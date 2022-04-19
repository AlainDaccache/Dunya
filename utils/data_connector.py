from abc import ABCMeta, abstractmethod
import re
import pandas as pd
import paramiko
from ftplib import FTP


class DataConnector():
    """
    A class used to represent a dataset in our Dunya.
    Configures and reads from different file systems, supports different formats,
    and returns appropriate data structure

    Attributes
    ----------
    file_system: str
        A transport protocol such as HTTP, FTP, SFTP

    Methods
    -------
    setup_file_system_connection(file_system, host=None, port=None, username=None, password=None)
        Sets up file system connection
    """

    def __init__(self, protocol: str):
        """
        Parameters
        ----------
        pass in ,
        """
        self.protocol = protocol

    @abstractmethod
    def setup_file_system_connection(self):
        """
        Initiate a connection between the remote and local systems
        """
        pass

    @abstractmethod
    def load_dataset(self, dataset_config, path, format, data_struct, **kwargs):
        pass


class LocalConnector(DataConnector):
    def __init__(self):
        super().__init__(protocol='Local')


class FTPConnector(DataConnector):
    """
     For secure transmission that protects the username and password, and encrypts the content,
     FTP is often secured with SSL/TLS (FTPS) or replaced with SSH File Transfer Protocol (SFTP).
    """

    def __init__(self, host: str = None, port: str = None, username: str = None, password: str = None):
        super().__init__(protocol='SFTP')
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connector = None

    def setup_file_system_connection(self, **kwargs) -> FTP:
        ftp = FTP(host=self.host, **kwargs)
        ftp.login(user=self.username, passwd=self.password, **kwargs)
        self.connector = ftp
        return ftp

    def load_dataset(self, input_path: str, output_path, output_format, data_struct, **kwargs):
        if self.connector is None:
            raise Exception('Connection has not been established yet')
        if not isinstance(self.connector, FTP):
            raise Exception('Connector should be of type `ftplib.FTP`')

        ftp = self.connector
        # separate the directory path and the file name, since ftp has to change working directory (cwd) before reading
        directory_path, file_name = '/'.join(input_path.split(sep='/')[:-1]), input_path.split(sep='/')[-1]
        ftp.cwd(directory_path)  # change working directory to file's location
        with open(file_name, 'wb') as fp:  # get the file
            ftp.retrbinary('RETR README', fp.write)

        return data

    def __del__(self):
        self.connector.quit()


class SFTPConnector(DataConnector):
    def __init__(self, host=None, port=None, username=None, password=None):
        super().__init__(protocol='SFTP')
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connector = None

    def setup_file_system_connection(self, host=None, port=None, username=None, password=None):
        transport = paramiko.Transport(sock=(self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        self.connector = transport
        return transport

    def load_dataset(self, dataset_config, path, format, data_struct, **kwargs):
        if self.connector is None:
            raise Exception('Connection has not been established yet')
        if not isinstance(self.connector, paramiko.Transport):
            raise Exception('Connector should be of type `paramiko.Transport`')
        transport = self.connector

        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp


class KafkaConnector(DataConnector):
    pass

