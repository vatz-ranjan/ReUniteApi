import mongoengine

mongoengine.register_connection(host='mongodb+srv://vatz:vatz@cluster0.usw9cmv.mongodb.net/?retryWrites=true&w=majority', alias='core', name='MissingChild')
# mongoengine.register_connection(alias='core', name='Helper')
