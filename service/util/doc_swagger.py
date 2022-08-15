from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', 
  { "a" : fields.Float(required=True, description="parametro a"), "b" : fields.Float(required=True, description="parametro b"),"c" : fields.Float(required=True, description="parametro c")}  
  )
