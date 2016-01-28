# tunables
	project						= 'testcovex'
	path						= "/vagrant"
	box 						= "bento/fedora-22"
# end tunables

unless Vagrant.has_plugin?("vagrant-hostmanager")
	raise "vagrant-hostmanager plugin is not installed. Please install it with: vagrant plugin install vagrant-hostmanager"
end

Vagrant.configure("2") do |config|

	config.vm.box				= box

	config.vm.synced_folder ".", "/vagrant", :disabled => true
	config.vm.synced_folder ".", path, :nfs => true
	config.vm.hostname = "#{project}.local"
	config.vm.network "private_network", :auto_network => true
	config.hostmanager.enabled = true
	config.hostmanager.manage_host = true

	config.ssh.forward_agent = true
	config.ssh.insert_key = false
end