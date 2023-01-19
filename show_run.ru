cisco = Cisco::Base.new(:host => "10.0.0.50", :password => "ciscotest")
cisco.cmd("sh ver")
cisco.enable("enablepass")
cisco.cmd("sh run")
output = cisco.run