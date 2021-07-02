from unittest import mock
import Chatrooms

def test_chatroom_instantiation():
    test_room = Chatrooms.Chatroom('test')
    assert test_room.name == 'test'
    assert test_room.client_sockets == []
    assert test_room.client_list == {}

def test_irc_application_instantiation():
    irc = Chatrooms.IRC_Application()
    assert irc.rooms == {}

def test_add_room():
    irc = Chatrooms.IRC_Application()
    mock_socket = mock.Mock()
    irc.create_room('#test_room', mock_socket, 'test_name')
    assert '#test_room' in irc.rooms

def test_join_room_wrong_name():
    mock_socket = mock.Mock()
    irc = Chatrooms.IRC_Application()
    irc.join_room('test_room', mock_socket, 'test_name')
    assert irc.rooms == {}

def test_join_room_create_room():
    mock_socket = mock.Mock()
    irc = Chatrooms.IRC_Application()
    irc.join_room('#test_room', mock_socket, 'test_name')
    assert '#test_room' in irc.rooms

def test_list_all_rooms_empty():
    irc = Chatrooms.IRC_Application()
    assert irc.list_all_rooms() == '\n'

def test_message_broadcast():
    ...
