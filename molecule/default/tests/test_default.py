import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'duf'
PACKAGE_BINARY = "/usr/bin/duf"


def test_duf_package_installed(host):
    """
    Tests if duf package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_duf_binary_exists(host):
    """
    Tests if duf binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_duf_binary_file(host):
    """
    Tests if duf binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_duf_binary_which(host):
    """
    Tests the output to confirm duf's binary location.
    """
    assert host.check_output('which duf') == PACKAGE_BINARY
