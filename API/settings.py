

MONGO_HOST = 'localhost'
MONGO_PORT = 27017


MONGO_DBNAME = 'data'

ITEM_METHODS = ['GET','PUT']

RESOURCE_METHODS = ['GET', 'POST']


datas = {

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'schema': {
        
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            # talk about hard constraints! For the purpose of the demo
            # 'lastname' is an API entry-point, so we need it to be unique.
            'unique': True,
        },
    }
}

DOMAIN = {'test': datas,}