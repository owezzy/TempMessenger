from nameko.rpc import rpc
from .dependencies.redis import MessageStore


class MessageService:

    name = 'message_service'
    message_store = MessageStore()

    @rpc
    def get_message(self, message_id):
        return self.message_store.get_message(message_id)

    @rpc
    def save_message(self, message):
        message_id = self.message_store.save_message(message)
        return message_id
