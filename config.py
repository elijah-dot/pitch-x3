import os

class Config:
    SECRET_KEY='885'
    SQLALCHEMY_DATABASE_URI = 'postgres://kzftmbyeacyolt:934aee6a457a0561bbf0a00cf5bfd0deb8bd65f5d5deefcb5ba19b8887774811@ec2-34-236-94-53.compute-1.amazonaws.com:5432/ddvq3evhnj0fum'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:just@localhost/beem'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # SQLALCHEMY_DATABASE_URI = 'postgres://mchocezjfxzarl:a9b935d4e036cca5080ed17a14a954ccd97d7ba3a13027f961e36188b8efebf2@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d5gamob8slp5c4'
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME='elijahwangu91@gmail.com'
    MAIL_PASSWORD='Elijah2000!'
    SUBJECT_PREFIX = 'pitch'
    SENDER_EMAIL = 'elijahwangu91@gmail.com'

    
   
    @staticmethod
    def init_app(app):
        pass


    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:just@localhost/beem'
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
     uri = uri.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI=uri 


class TestConfig(Config):
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:just@localhost/beem'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
