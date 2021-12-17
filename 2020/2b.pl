#!/opt/local/bin/perl

$i = 0;
while(<>)
{
	/^([0-9]+)-([0-9]+) ([a-z]): (.*)/;
   $one = $1; $two = $2;
   $ch  = $3; $str = $4;
   $a = substr $str, ($one-1), 1;
   $b = substr $str, ($two-1), 1;
   $i++ if ($a eq $ch || $b eq $ch) && !($a eq $b);
}

print "$i\n";
