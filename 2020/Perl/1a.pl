my $a, $b;
my %h;

while(<>)
{
	$a = int($_);
   $b = 2020 - $a;
   if (exists $h{$b})
   {
      $c = $a * $b;
		print "$a, $b, $c\n";
   }

	$h{$a} = 1;
}
