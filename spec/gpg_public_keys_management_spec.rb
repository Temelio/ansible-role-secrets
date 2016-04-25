require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'secrets Ansible role - SSH private keys' do

    # Declare variables
    present_gpg_keys = Array[ '2048R/3488F25B', '2048R/D1CE33EC' ]
    absent_gpg_keys = Array[ '7D3DD982' ]

    describe command('sudo -u root gpg --list-keys') do

        present_gpg_keys.each do |key_id|
            its(:stdout) { should match /.*#{key_id}.*/ }
        end

        absent_gpg_keys.each do |key_id|
            its(:stdout) { should_not match /.*#{key_id}.*/ }
        end
    end
end

