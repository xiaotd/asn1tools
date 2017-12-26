RFC3161 = {'PKIXTSP': {'extensibility-implied': False,
             'imports': {'CryptographicMessageSyntax': ['ContentInfo'],
                         'PKIX1Explicit88': ['Extensions',
                                             'AlgorithmIdentifier'],
                         'PKIX1Implicit88': ['GeneralName'],
                         'PKIXCMP': ['PKIFreeText']},
             'object-classes': {},
             'object-sets': {},
             'tags': 'IMPLICIT',
             'types': {'Accuracy': {'members': [{'name': 'seconds',
                                                 'optional': True,
                                                 'type': 'INTEGER'},
                                                {'name': 'millis',
                                                 'optional': True,
                                                 'restricted-to': [(1,
                                                                    999)],
                                                 'tag': {'number': 0},
                                                 'type': 'INTEGER'},
                                                {'name': 'micros',
                                                 'optional': True,
                                                 'restricted-to': [(1,
                                                                    999)],
                                                 'tag': {'number': 1},
                                                 'type': 'INTEGER'}],
                                    'type': 'SEQUENCE'},
                       'MessageImprint': {'members': [{'name': 'hashAlgorithm',
                                                       'optional': False,
                                                       'type': 'AlgorithmIdentifier'},
                                                      {'name': 'hashedMessage',
                                                       'optional': False,
                                                       'size': None,
                                                       'type': 'OCTET STRING'}],
                                          'type': 'SEQUENCE'},
                       'PKIFailureInfo': {'size': None,
                                          'type': 'BIT STRING'},
                       'PKIStatus': {'type': 'INTEGER'},
                       'PKIStatusInfo': {'members': [{'name': 'status',
                                                      'optional': False,
                                                      'type': 'PKIStatus'},
                                                     {'name': 'statusString',
                                                      'optional': True,
                                                      'type': 'PKIFreeText'},
                                                     {'name': 'failInfo',
                                                      'optional': True,
                                                      'type': 'PKIFailureInfo'}],
                                         'type': 'SEQUENCE'},
                       'TSAPolicyId': {'type': 'OBJECT IDENTIFIER'},
                       'TSTInfo': {'members': [{'name': 'version',
                                                'optional': False,
                                                'type': 'INTEGER'},
                                               {'name': 'policy',
                                                'optional': False,
                                                'type': 'TSAPolicyId'},
                                               {'name': 'messageImprint',
                                                'optional': False,
                                                'type': 'MessageImprint'},
                                               {'name': 'serialNumber',
                                                'optional': False,
                                                'type': 'INTEGER'},
                                               {'name': 'genTime',
                                                'optional': False,
                                                'type': 'GeneralizedTime'},
                                               {'name': 'accuracy',
                                                'optional': True,
                                                'type': 'Accuracy'},
                                               {'default': 'FALSE',
                                                'name': 'ordering',
                                                'optional': False,
                                                'type': 'BOOLEAN'},
                                               {'name': 'nonce',
                                                'optional': True,
                                                'type': 'INTEGER'},
                                               {'name': 'tsa',
                                                'optional': True,
                                                'tag': {'number': 0},
                                                'type': 'GeneralName'},
                                               {'name': 'extensions',
                                                'optional': True,
                                                'tag': {'kind': 'IMPLICIT',
                                                        'number': 1},
                                                'type': 'Extensions'}],
                                   'type': 'SEQUENCE'},
                       'TimeStampReq': {'members': [{'name': 'version',
                                                     'optional': False,
                                                     'type': 'INTEGER'},
                                                    {'name': 'messageImprint',
                                                     'optional': False,
                                                     'type': 'MessageImprint'},
                                                    {'name': 'reqPolicy',
                                                     'optional': True,
                                                     'type': 'TSAPolicyId'},
                                                    {'name': 'nonce',
                                                     'optional': True,
                                                     'type': 'INTEGER'},
                                                    {'default': 'FALSE',
                                                     'name': 'certReq',
                                                     'optional': False,
                                                     'type': 'BOOLEAN'},
                                                    {'name': 'extensions',
                                                     'optional': True,
                                                     'tag': {'kind': 'IMPLICIT',
                                                             'number': 0},
                                                     'type': 'Extensions'}],
                                        'type': 'SEQUENCE'},
                       'TimeStampResp': {'members': [{'name': 'status',
                                                      'optional': False,
                                                      'type': 'PKIStatusInfo'},
                                                     {'name': 'timeStampToken',
                                                      'optional': True,
                                                      'type': 'TimeStampToken'}],
                                         'type': 'SEQUENCE'},
                       'TimeStampToken': {'type': 'ContentInfo'}},
             'values': {'id-ct-TSTInfo': {'type': 'OBJECT IDENTIFIER',
                                          'value': [('iso', 1),
                                                    ('member-body', 2),
                                                    ('us', 840),
                                                    ('rsadsi', 113549),
                                                    ('pkcs', 1),
                                                    ('pkcs-9', 9),
                                                    ('smime', 16),
                                                    ('ct', 1),
                                                    4]}}}}
