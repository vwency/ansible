import pytest
import warnings
import os
import testinfra.utils.ansible_runner
 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 

@pytest.mark.parametrize("postgres_installed", [
    ("postgresql16"),
])


@pytest.mark.limit('preprod-study-ansible-705')
def test_packages(host, postgres_installed):
    # if host.backend.get_connection_type() == "ansible":
    #     if host.backend.get_hostname() != 'preprod-study-ansible-705':
    #         pytest.skip("Skipped, != preprod-study-ansible-705")
    psql = host.package(postgres_installed)

    assert psql.is_installed


@pytest.mark.parametrize("postgres_service_check", [
    ("postgresql-16"),
])

@pytest.mark.limit('preprod-study-ansible-705')
def test_packages(host, postgres_service_check):
    # if host.backend.get_connection_type() == "ansible":
    #     if host.backend.get_hostname() != 'preprod-study-ansible-705':
    #         pytest.skip("Skipped, != preprod-study-ansible-705")
    psql = host.service(postgres_service_check)

    assert psql.is_running
    assert psql.is_enabled

























# This suppresses about 80% of the deprecation warnings from python 3.7.
# import warnings



# def test__running_and_enabled(host):
#     psql = host.service("postgresql-16")
#     assert psql.is_running
#     assert psql.is_enabled



# def test_hosts_file(host):
#     f = host.file('/etc/hosts')

#     # EXAMPLE_7 break TestInfra by testing that /etc/hosts does not esist
#     assert f.exists is not True
#     assert f.user == 'root'
#     assert f.group == 'root'


# @pytest.mark.parametrize('name', ['which', 'iproute'])
# def test_base_packages(host, name):
#     p = host.package(name)
#
#     assert p.is_installed 


# def test_which_package(host):
#     p = host.package('which')

#     assert p.is_installed


# def test_iproute_package(host):
#     p = host.package('iproute')

#     assert p.is_installed