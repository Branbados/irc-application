import Client

def test_client_instantiation():
    test_client = Client.Client('test_name','test_host', 'test_port', 'test_socket')
    assert test_client.name == 'test_name'
    assert test_client.host == 'test_host'
    assert test_client.port == 'test_port'
    assert test_client.server_socket == 'test_socket'

def test_client_from_input():
    ...