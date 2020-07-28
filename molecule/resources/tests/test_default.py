import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

def test_package_is_installed(host):
    logstash = host.package('logstash')

    assert logstash.is_installed
    assert logstash.version.startswith('7')


def test_service_is_running_and_enabled(host):
    logstash = host.service("logstash")

    assert logstash.is_running
    assert logstash.is_enabled
