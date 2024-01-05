
while(<>)
{
	chomp;
	$line = "." . $_ . "." ;
	push @m, [split //, $line];
}
$rows = $#m + 1;
$cols = $#{$m[0]} + 1;

push @m, [split //, ("." x $cols)];
unshift @m, [split //, ("." x $cols)];

$rows = $#m + 1;
$cols = $#{$m[0]} + 1;

# print "$rows, $cols\n\n";

for ($i = 0; $i < 10; $i++)
{
	print "$i\n";
	for ($r = 0; $r < $rows; $r++)
	{
		for ($c = 0; $c < $cols; $c++)
		{
			print "$m[$r][$c]";
		}
		print "\n";
	} 
	print "\n\n";
	for ($r = 0; $r < $rows; $r++)
	{
		for ($c = 0; $c < $cols; $c++)
		{
			$p[$r][$c] = $m[$r][$c];
	
			next if $m[$r][$c] eq ".";
	
			$count = 0;
			@a = qw(-1 0 1);
			foreach $dx (@a)
			{
			   foreach $dy (@a)
			   {
					$count += ($m[$r+$dx][$c+$dy] eq "#") ? 1 : 0;
			   }
			}
			if ($m[$r][$c] eq "L" && $count == 0)
			{
				$p[$r][$c] = "#";
			}
			if ($p[$r][$c] eq "#" && $count >= 5)
			{
				$p[$r][$c] = "L";
			}
		}
	}

	@m = @p;
}
