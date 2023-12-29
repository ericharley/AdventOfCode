while(<>)
{
chomp;
($left,$right) = split / -> /;
$left =~ s/^(%|&)//;
@list = split /, /,$right;
#print "$left||@list\n";
foreach $b (@list){
print "$left -> $b\n";
}
}
