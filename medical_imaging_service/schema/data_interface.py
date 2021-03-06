import objectpath

class DataQuery:

    tree = None

    def __init__(self, json_data):
        self.tree = objectpath.Tree(json_data)

    def queryObjectTree(self, json_query):

        results = list(self.tree.execute(json_query))

        return results

    def getObjectFilterString(self, argument_dictionary: dict):

        filter_string = ""
        i = 1

        if len(argument_dictionary.items()) > 0:
            filter_string = "["

            for k, v in argument_dictionary.items():
                if type(v) == str:
                    v = "'{v}'".format(v=v)

                filter_string = filter_string + "@.{k} is {v}".format(k=k, v=v)

                if i < len(argument_dictionary.items()):
                    filter_string = filter_string + " and "

                i += 1

            filter_string = filter_string + "]"

        return filter_string

class DataStorage:

    data = None
    dq = None

    def __init__(self):
        self.loadData()
        self.dq = DataQuery(json_data=self.data)

    def loadData(self):

        self.data = [
            {'id': 666, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0000.dcm'},
            {'id': 667, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0001.dcm'},
            {'id': 668, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0002.dcm'},
            {'id': 669, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0003.dcm'},
            {'id': 670, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0004.dcm'},
            {'id': 671, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0005.dcm'},
            {'id': 672, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0006.dcm'},
            {'id': 673, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0007.dcm'},
            {'id': 674, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0008.dcm'},
            {'id': 675, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0009.dcm'},
            {'id': 676, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0010.dcm'},
            {'id': 677, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0011.dcm'},
            {'id': 678, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0012.dcm'},
            {'id': 679, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0013.dcm'},
            {'id': 680, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0014.dcm'},
            {'id': 681, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0015.dcm'},
            {'id': 682, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0016.dcm'},
            {'id': 683, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0017.dcm'},
            {'id': 684, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0018.dcm'},
            {'id': 685, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0019.dcm'},
            {'id': 686, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0020.dcm'},
            {'id': 687, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0021.dcm'},
            {'id': 688, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0022.dcm'},
            {'id': 689, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0023.dcm'},
            {'id': 690, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0024.dcm'},
            {'id': 691, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0025.dcm'},
            {'id': 692, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0026.dcm'},
            {'id': 693, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0027.dcm'},
            {'id': 694, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0028.dcm'},
            {'id': 695, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0029.dcm'},
            {'id': 696, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0030.dcm'},
            {'id': 697, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0031.dcm'},
            {'id': 698, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0032.dcm'},
            {'id': 699, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0033.dcm'},
            {'id': 700, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0034.dcm'},
            {'id': 701, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0035.dcm'},
            {'id': 702, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0036.dcm'},
            {'id': 703, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0037.dcm'},
            {'id': 704, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0038.dcm'},
            {'id': 705, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0039.dcm'},
            {'id': 706, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0040.dcm'},
            {'id': 707, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0041.dcm'},
            {'id': 708, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0042.dcm'},
            {'id': 709, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0043.dcm'},
            {'id': 710, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0044.dcm'},
            {'id': 711, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0045.dcm'},
            {'id': 712, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0046.dcm'},
            {'id': 713, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0047.dcm'},
            {'id': 714, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0048.dcm'},
            {'id': 715, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0049.dcm'},
            {'id': 716, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0050.dcm'},
            {'id': 717, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0051.dcm'},
            {'id': 718, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0052.dcm'},
            {'id': 719, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0053.dcm'},
            {'id': 720, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0054.dcm'},
            {'id': 721, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0055.dcm'},
            {'id': 722, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0056.dcm'},
            {'id': 723, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0057.dcm'},
            {'id': 724, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0058.dcm'},
            {'id': 725, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0059.dcm'},
            {'id': 726, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0060.dcm'},
            {'id': 727, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0061.dcm'},
            {'id': 728, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0062.dcm'},
            {'id': 729, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0063.dcm'},
            {'id': 730, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0064.dcm'},
            {'id': 731, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0065.dcm'},
            {'id': 732, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0066.dcm'},
            {'id': 733, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0067.dcm'},
            {'id': 734, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0068.dcm'},
            {'id': 735, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0069.dcm'},
            {'id': 736, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0070.dcm'},
            {'id': 737, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0071.dcm'},
            {'id': 738, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0072.dcm'},
            {'id': 739, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0073.dcm'},
            {'id': 740, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0074.dcm'},
            {'id': 741, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0075.dcm'},
            {'id': 742, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0076.dcm'},
            {'id': 743, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0077.dcm'},
            {'id': 744, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0078.dcm'},
            {'id': 745, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0079.dcm'},
            {'id': 746, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0080.dcm'},
            {'id': 747, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0081.dcm'},
            {'id': 748, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0082.dcm'},
            {'id': 749, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0083.dcm'},
            {'id': 750, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0084.dcm'},
            {'id': 751, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0085.dcm'},
            {'id': 752, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0086.dcm'},
            {'id': 753, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0087.dcm'},
            {'id': 754, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0088.dcm'},
            {'id': 755, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0089.dcm'},
            {'id': 756, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0090.dcm'},
            {'id': 757, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0091.dcm'},
            {'id': 758, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0092.dcm'},
            {'id': 759, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0093.dcm'},
            {'id': 760, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0094.dcm'},
            {'id': 761, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0095.dcm'},
            {'id': 762, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0096.dcm'},
            {'id': 763, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0097.dcm'},
            {'id': 764, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0098.dcm'},
            {'id': 765, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0099.dcm'},
            {'id': 766, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0100.dcm'},
            {'id': 767, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0101.dcm'},
            {'id': 768, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0102.dcm'},
            {'id': 769, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0103.dcm'},
            {'id': 770, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0104.dcm'},
            {'id': 771, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0105.dcm'},
            {'id': 772, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0106.dcm'},
            {'id': 773, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0107.dcm'},
            {'id': 774, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0108.dcm'},
            {'id': 775, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0109.dcm'},
            {'id': 776, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0110.dcm'},
            {'id': 777, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0111.dcm'},
            {'id': 778, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0112.dcm'},
            {'id': 779, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0113.dcm'},
            {'id': 780, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0114.dcm'},
            {'id': 781, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0115.dcm'},
            {'id': 782, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0116.dcm'},
            {'id': 783, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0117.dcm'},
            {'id': 784, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0118.dcm'},
            {'id': 785, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0119.dcm'},
            {'id': 786, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0120.dcm'},
            {'id': 787, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0121.dcm'},
            {'id': 788, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0122.dcm'},
            {'id': 789, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0123.dcm'},
            {'id': 790, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0124.dcm'},
            {'id': 791, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0125.dcm'},
            {'id': 792, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0126.dcm'},
            {'id': 793, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0127.dcm'},
            {'id': 794, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0128.dcm'},
            {'id': 795, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0129.dcm'},
            {'id': 796, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0130.dcm'},
            {'id': 797, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0131.dcm'},
            {'id': 798, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0132.dcm'},
            {'id': 799, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0133.dcm'},
            {'id': 800, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0134.dcm'},
            {'id': 801, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0135.dcm'},
            {'id': 802, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0136.dcm'},
            {'id': 803, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0137.dcm'},
            {'id': 804, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0138.dcm'},
            {'id': 805, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0139.dcm'},
            {'id': 806, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0140.dcm'},
            {'id': 807, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0141.dcm'},
            {'id': 808, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0142.dcm'},
            {'id': 809, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0143.dcm'},
            {'id': 810, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0144.dcm'},
            {'id': 811, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0145.dcm'},
            {'id': 812, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0146.dcm'},
            {'id': 813, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0147.dcm'},
            {'id': 814, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0148.dcm'},
            {'id': 815, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0149.dcm'},
            {'id': 816, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0150.dcm'},
            {'id': 817, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0151.dcm'},
            {'id': 818, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0152.dcm'},
            {'id': 819, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0153.dcm'},
            {'id': 820, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0154.dcm'},
            {'id': 821, 'user_id': 100, 'type': 'MRI_T1c', 'format': 'DICOM',
             'url': 'https://medical-imaging-service.s3.amazonaws.com/mock-sources/source-01/IMG0155.dcm'}
        ]

    def getMedicalImage(self, **kwargs):
        filter_string = self.dq.getObjectFilterString(argument_dictionary=kwargs)

        json_query = "$.*{filters}".format(filters=filter_string)

        return self.dq.queryObjectTree(json_query=json_query)