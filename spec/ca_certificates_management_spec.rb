require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'secrets Ansible role' do

    # Declare variables
    yaml_name = ''
    file_name = ''
    owner = ''
    group = ''
    mode = 644

    if ['debian', 'ubuntu'].include?(os[:family])
        yaml_name = '/etc/ssl/certs/secrets_test_ca_management_from_yml.crt'
        file_name = '/etc/ssl/certs/secrets_test_ca_management_from_file.crt'
        owner = 'root'
        group = 'root'
    end

    describe file(yaml_name) do
        it { should exist }
        it { should be_file }
        it { should be_owned_by owner }
        it { should be_grouped_into group }
        it { should be_mode mode }
    end

    describe file(file_name) do
        it { should exist }
        it { should be_file }
        it { should be_owned_by owner }
        it { should be_grouped_into group }
        it { should be_mode mode }
    end
end

