# input ; "Valve XC has flow rate=0; tunnels lead to valves YK, AM"

# output "XC": (0, ["YK", "AM"])

while(<>)
{
  chomp;
  if ( /^Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.*?)$/ )
  {
#    print "$_\n";
#    print "|$1|, |$2|, |$3|\n";
#    |UU|, |15|, |QZ, IB, ME|
    @a = split /, /, $3;
    $s = join "\", \"", @a;
#    print "|$3|->\"$s\"\n";
    print "\"$1\": ($2, [$s]), "
  }
}
