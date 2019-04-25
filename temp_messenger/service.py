from nameko.rpc import rpc


class KonnichiwaService:

    name = 'konnnichiwa_service'

    @rpc
    def konnichiwa(self):
        return 'Konnichiwa!'

