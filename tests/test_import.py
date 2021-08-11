def test_netmiko_import():
    import netmiko

    assert "3.4" in netmiko.__version__
