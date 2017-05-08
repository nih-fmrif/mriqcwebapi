import os
import re
get_mongo_host = re.match('tcp://(.*):(.*)', os.environ['MONGODB_PORT'])

my_settings = {
    'MONGO_HOST': get_mongo_host.group(1),
    'MONGO_PORT': get_mongo_host.group(2),
    'MONGO_DBNAME': 'scenarios',
    'X_DOMAINS': '*',
    'DOMAIN': {
        'scenarios': {
            'item_title': 'scenario',
            'resource_methods': ['GET', 'POST'],
            'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
            'schema': {
                # 'title': {
                #     'type': 'string',
                #     'minlength': 1,
                #     'maxlength': 100,
                #     'required': True
                # },
                'cjv':{
                    'type': 'float',
                    'required': True
                },
                'cnr':{
                    'type':'float',
                    'required': True
                },
                'efc':{
                    'type':'float',
                    'required': True
                },
                'fber': {
                    'type': 'float',
                    'required': True
                },
                'fwhm_avg': {
                    'type': 'float',
                    'required': True
                },
                'fwhm_x':{
                    'type': 'float',
                    'required': True
                },
                'fwhm_y': {
                    'type': 'float',
                    'required': True
                },
                'fwhm_z': {
                    'type': 'float',
                    'required': True
                },
                'icvs_csf': {
                    'type': 'float',
                    'required': True
                },
                'icvs_gm': {
                    'type': 'float',
                    'required': True
                },
                'icvs_wm': {
                    'type': 'float',
                    'required': True
                },
                'inu_med': {
                    'type': 'float',
                    'required': True
                },
                'inu_range': {
                    'type': 'float',
                    'required': True
                },
            # 'SliceTiming': {'type': 'list[float]'},
            'DeviceSerialNumber': {'type': 'string'},
            'EchoTime': {'type': 'float'},
            'FlipAngle': {'type': 'integer'},
            'InversionTime': {'type': 'float'},
            'MagneticFieldStrength': {'type': 'integer'},
            'ManufacturerModelName': {'type': 'string'},
            'PhaseEncodingDirection': {'type': 'string'},
            'ReceiveCoilName': {'type': 'string'},
            'RepetitionTime': {'type': 'float'},
            'SoftwareVersions': {'type': 'string'},
            'ContrastBolusIngredient':  {'type': 'string'},
            'TaskName': {'type': 'string'},
            'Manufacturer': {'type': 'string'},
            'HardcopyDeviceSoftwareVersion': {'type': 'string'},
            'GradientSetType': {'type': 'string'},
            'MRTransmitCoilSequence':{'type': 'string'},
            'MatrixCoilMode': {'type': 'string'},
            'CoilCombinationMethod': {'type': 'string'},
            'PulseSequenceType': {'type': 'string'},
            'PulseSequenceDetails': {'type': 'string'},
            'NumberShots' :{'type': 'integer'},
            'ParallelReductionFactorInPlane':{'type': 'float'},
            'ParallelAcquisitionTechnique': {'type': 'string'},
            'PartialFourier' :{'type': 'boolean'},
            'PartialFourierDirection':{'type': 'string'},
            'EffectiveEchoSpacing' :{'type': 'float'},
            'TotalReadoutTime':{'type': 'float'},
            'SliceEncodingDirection': {'type': 'string'},
            'NumberOfVolumesDiscardedByScanner':{'type': 'float'},
            'NumberOfVolumesDiscardedByUser':{'type': 'float'},
            'DelayTime':{'type': 'float'},
            'MultibandAccelerationFactor':{'type': 'float'},
            'Instructions': {'type': 'string'},
            'TaskDescription': {'type': 'string'},
            'CogAtlasID' : {'type': 'string'},
            'CogPOID': {'type': 'string'},
            'InstitutionName': {'type': 'string'},
            'InstitutionAddress': {'type': 'string'},
            'ConversionSoftware': {'type': 'string'},
            'ConversionSoftwareVersion': {'type': 'string'},
            'md5sum' :{'type': 'float'},
            'modality': {'type': 'string'},
            'mriqc_pred' : {'type':'boolean'},
            'software': {'type': 'string'},
            'subject_id': {'type': 'string'},
            'version' : {'type': 'string'},

                # required data 
                'md5sum': {
                    'type': 'string',
                    'required': True
                },
                'modality': {
                    'type': 'string',
                    'required': True
                },
                'mriqc_pred': {
                    'type': 'integer',
                    'required': True
                },
                'software': {
                    'type': 'string',
                    'required': True
                },
                'subject_id': {
                    'type': 'string',
                    'required': True
                },
                'version': {
                    'type': 'string',
                    'required': True
                },
                'qi_1': {
                    'type': 'float',
                    'required': True
                },
                'qi_2': {
                    'type': 'float',
                    'required': True
                },
                'rpve_csf': {
                    'type': 'float',
                    'required': True
                },
                'rpve_gm': {
                    'type': 'float',
                    'required': True
                },
                'rpve_wm': {
                    'type': 'float',
                    'required': True
                },
                'size_x': {
                    'type': 'integer',
                    'required': True
                },
                'size_y': {
                    'type': 'integer',
                    'required': True
                },
                'size_z': {
                    'type': 'integer',
                    'required': True
                },
                'snr_csf': {
                    'type': 'float',
                    'required': True
                },
                'snr_gm': {
                    'type': 'float',
                    'required': True
                },
                'snr_total':{
                    'type': 'float',
                    'required': True
                },
                'snr_wm': {
                    'type': 'float',
                    'required': True
                },
                'snrd_csf': {
                    'type': 'float',
                    'required': True
                },
                'snrd_gm': {
                    'type': 'float',
                    'required': True
                },
                'snrd_total': {
                    'type': 'float',
                    'required': True
                },
                'snrd_wm': {
                    'type': 'float',
                    'required': True
                },
                'spacing_x': {
                    'type': 'float',
                    'required': True
                },
                'spacing_y': {
                    'type': 'float',
                    'required': True
                },
                'spacing_z': {
                    'type': 'float',
                    'required': True
                },
                'summary_bg_k': {
                    'type': 'float',
                    'required': True    
                },
                'summary_bg_mean': {
                    'type': 'float',
                    'required': True
                },
                'summary_bg_p05': {
                    'type': 'float',
                    'required': True
                },
                'summary_bg_p95': {
                    'type': 'float',
                    'required': True
                },
                'summary_bg_stdv': {
                    'type': 'float',
                    'required': True
                },
                'summary_csf_k': {
                    'type': 'float',
                    'required': True
                },
                'summary_csf_mean': {
                    'type': 'float',
                    'required': True
                },
                'summary_csf_p05': {
                    'type': 'float',
                    'required': True
                },
                'summary_csf_p95': {
                    'type': 'float',
                    'required': True
                },
                'summary_csf_stdv': {
                    'type': 'float',
                    'required': True
                },
                'summary_gm_k': {
                    'type': 'float',
                    'required': True    
                },
                'summary_gm_mean': {
                    'type': 'float',
                    'required': True
                },
                'summary_gm_p05': {
                    'type': 'float',
                    'required': True
                },
                'summary_gm_p95': {
                    'type': 'float',
                    'required': True
                },
                'summary_gm_stdv': {
                    'type': 'float',
                    'required': True
                },
                'summary_wm_k': {
                    'type': 'float',
                    'required': True
                },
                'summary_wm_mean':{
                    'type': 'float',
                    'required': True
                },
                'summary_wm_p05': {
                    'type': 'float',
                    'required': True
                },
                'summary_wm_p95': {
                    'type': 'float',
                    'required': True
                },
                'summary_wm_stdv': {
                    'type': 'float',
                    'required': True
                },
                'tpm_overlap_csf':{
                    'type': 'float',
                    'required': True
                },
                'tpm_overlap_gm': {
                    'type': 'float',
                    'required': True
                },
                'tpm_overlap_wm': {
                    'type': 'float',
                    'required': True
                },
                'wm2max':{
                    'type': 'float',
                    'required': True
                },
            }
        }
    }
}

