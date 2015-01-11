from google.appengine.ext import ndb

# import yawp from yawp
# yawp('/people').query().fetch()
# http://stackoverflow.com/questions/10709893/ndb-expando-model-with-dynamic-textproperty
# http://stackoverflow.com/questions/19842671/migrating-data-when-changing-an-ndb-fields-property-type/19848970#19848970

def yawp(path):
    def _get_kind(cls):
        return path

    def change_type(self, key, new_type):
        self._properties[key] = new_type(key)

    Model = type(path, (ndb.Expando,), {'change_type':change_type})
    Model._get_kind = classmethod(_get_kind)
    return Model
