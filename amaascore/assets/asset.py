import datetime
import uuid

from amaascore.core.amaas_model import AMaaSModel
from amaascore.core.reference import Reference


class Asset(AMaaSModel):

    @staticmethod
    def children():
        return ['charges', 'codes', 'references']

    def __init__(self, asset_manager_id, asset_class, fungible, asset_issuer_id, asset_id=None, asset_status='Active',
                 version=1, country_id=None, venue_id=None, maturity_date=None,
                 description='', references={}, *args, **kwargs):
        self.additional_dict = {}
        self.asset_manager_id = asset_manager_id
        self.asset_id = asset_id or uuid.uuid4().hex
        self.asset_class = asset_class
        self.asset_type =  self.__class__.__name__
        self.fungible = fungible
        self.asset_issuer_id = asset_issuer_id
        self.asset_status = asset_status
        self.version = version
        self.country_id = country_id
        self.venue_id = venue_id
        self.maturity_date = maturity_date or datetime.date.max  # Has to be here to prevent arg binding
        self.description = description
        self.references = references
        self.references['AMaaS'] = Reference(reference_value=self.asset_id)  # Upserts the AMaaS Reference

        super(Asset, self).__init__(*args, **kwargs)

    def reference_types(self):
        """
        TODO - are these helper functions useful?
        :return:
        """
        return self.references.keys()

    def __str__(self):
        return "Asset object - ID: %s" % self.asset_id
