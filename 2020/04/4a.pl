#!/opt/local/bin/perl

$/ = "\n\n";

@fields = qw(byr iyr eyr hgt hcl ecl pid cid);

$c = 0;
while(<>)
{
  chomp;
  s/\n/ /g;
  %h = split /[ :]/;

  $v = 1;
  foreach $f (@fields)
  {
    $v = 0 unless exists $h{$f} || $f eq "cid";
  }
  $c += $v;
}

print "$c\n";
