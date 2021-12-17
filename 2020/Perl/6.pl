$/ = "\n\n";

$total = 0;

while(<>)
{
	chomp;
	my %hash;
	@lines = split /\n/;
#	$c = scalar @lines;
#	print "number of people: $c\n";
	foreach $line (@lines)
	{
		@questions = split //, $line;
		@hash{@questions} = @questions;
	}

	$num = scalar keys %hash;

#	foreach $key (sort keys %hash)
#	{
#		print "$key:$hash{$key}\n";
#	}

#	print "\n";

#	print "$num\n";

	$total += $num;

}

print "$total\n";
