class Development(object):
    DEBUG = True

    ## DB URL FOR DEVELOPMENT
    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@localhost/dbname'


class Testing(object):
    DEBUG = False
    
    ## DB URL FOR TESTING
    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@test/dbname'


class Production(object):
    DEBUG = False

    ## DB URL FOR PRODUCTION
    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@production/dbname'
