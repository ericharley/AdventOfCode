use strict;

my @h = sort {$a <=> $b} map int, split /\n/, `cat $ARGV[0]`;

foreach my $t (@h)
{
   my %g = {};
   foreach my $a (@h)
   {
     $b = 2020 - $t - $a;
     if (exists $g{$b})
     {
       my $c = $t * $a * $b;
       print "$t * $a * $b = $c\n";
       exit;
     }
     $g{$a} = 1;	
   }
}
