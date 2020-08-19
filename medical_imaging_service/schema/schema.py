from dataclasses import dataclass

from ariadne import ObjectType, QueryType, snake_case_fallback_resolvers
from ariadne_extensions.federation import FederatedManager, FederatedObjectType

from schema.data_interface import DataStorage

@dataclass
class BoundaryGeneric:

    def __init__(self, child_name, kwargs=None):
        self.typename = child_name

        if kwargs:
            self.update_class(kwargs)

        self.get_updated()

    def update_class(self, kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)

    def get_updated(self):
        return self


"""
Dataclasses, These need to be defined for Boundry Types (A GraphQL type from another server that you are Extending
"""
@dataclass
class Model(BoundaryGeneric):
    def __init__(self, **kwargs):
        super().__init__(self.__class__.__name__, kwargs)

"""
Creates the Schema and adds the Federation Declerations to it according to the [https://www.apollographql.com/docs/apollo-server/federation/federation-spec/](Apollo Spec).
"""
class SchemaCreator:

    query = QueryType()
    model = FederatedObjectType("Model")
    medicalImage = FederatedObjectType("MedicalImage")

    def __init__(self):
        self.ds = DataStorage()

    def getSchema(self):

        manager = FederatedManager(
            schema_sdl_file='schema/schema.graphql',
            query=self.query,
        )

        @self.query.field("medicalImage")
        def resolve_medical_image(*_, **kwargs):
           return self.ds.getMedicalImage(**kwargs)

        @self.model.resolve_reference
        def resolve_model(representation):
            user_id = representation.get('id')
            return Model(id=user_id)

        @self.model.field("medicalImages")
        def resolve_model_images(obj, info):
            kwargs = {
                "user_id": obj.id
            }

            return self.ds.getMedicalImage(**kwargs)

        manager.add_types(self.model, self.medicalImage)
        manager.add_types(snake_case_fallback_resolvers)

        return manager.get_schema()