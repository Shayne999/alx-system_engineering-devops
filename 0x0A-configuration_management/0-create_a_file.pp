#creates a file
file { '/tmp/school':
	mode => '0744',
	owner => 'www-data',
	grpupp => 'www-data',
	content => 'I love puppet'
}
