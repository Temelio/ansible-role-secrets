require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'secrets Ansible role - SSH private keys' do

    # Declare variables
    yaml_name = '/tmp/secrets_test_ssh_private_key_from_yml.key'
    file_name = '/tmp/secrets_test_ssh_private_key_from_file.key'
    absent_files = Array['/tmp/secrets_test_absent_ssh_private_key_from_yml.key',
                         '/tmp/secrets_test_absent_ssh_private_key_from_file.key']
    owner = 'root'
    group = 'root'
    mode = 400

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

    it 'remove keys with absent state' do
        absent_files.each do |filename|
            expect(file(filename)).to_not exist
        end
    end
end
