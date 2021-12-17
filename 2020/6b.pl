$/ = "\n\n";

$total = 0;

while(<>)
{
	chomp;

	my %hash;

	@lines = split /\n/;
	$c = scalar @lines;
	foreach $line (@lines)
	{
		@questions = split //, $line;
		foreach $q (@questions)
		{
			if ( exists $hash{$q} ) {
				@hash{$q}++;
			} else {
				@hash{$q} = 1;
			}
		}
	}

	$num = 0;
	foreach $key (sort keys %hash)
	{
		$num++ if ($hash{$key} == $c);
	}

	$total += $num;

}

print "$total\n";
