#!/opt/local/bin/perl

$i = 0;
while(<>)
{
  /^([0-9]+)-([0-9]+) ([a-z]): (.*)/;
  $low = $1; $hi = $2;
  $count = () = $4 =~ /$3/g;
  $i++ if ( $low <= $count && $count <= $hi );
}

print "$i\n";
