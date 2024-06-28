from app.dao.base import BaseDAO
from app.envelopes.models import Envelopes

class EnvelopeDAO(BaseDAO):
    model = Envelopes
           