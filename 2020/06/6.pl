$/ = "\n\n";

$total = 0;

while(<>)
{
	chomp;
	my %hash;
	@lines = split /\n/;
	foreach $line (@lines)
	{
		@questions = split //, $line;
		@hash{@questions} = @questions;
	}

	$num = scalar keys %hash;

	$total += $num;

}

print "$total\n";
