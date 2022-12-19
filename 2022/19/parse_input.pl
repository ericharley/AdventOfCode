while(<>)
{

chomp;

die unless /Blueprint ([0-9]+)/;
$n = $1;

die unless /Each ore robot costs ([0-9]+) ore/;
$o = $1;

die unless /Each clay robot costs ([0-9]+) ore/;
$c = $1;

die unless /Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay/;
$oo = $1;
$oc = $2;

die unless /Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian/;
$go = $1;
$gob = $2;

print <<"_END_";
#BP $n
if BP = $n:
 cost['ore_robot'] = Cost($o,0,0)
 cost['clay_robot'] = Cost($c,0,0)
 cost['obsidian_robot'] = Cost($oo,$oc,0)
 cost['geode_robot'] = Cost($go,0,$gob)

_END_

}
