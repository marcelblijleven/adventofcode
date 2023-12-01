from adventofcode.year_2021.day_19_2021 import (
    AxisOffset,
    Scanner,
    apply_offset,
    calculate_max_distance,
    count_unique_beacons,
    get_offset,
    get_scanners,
    part_one,
    part_two,
    process_scanners,
)

test_input = [
    "--- scanner 0 ---",
    "404,-588,-901",
    "528,-643,409",
    "-838,591,734",
    "390,-675,-793",
    "-537,-823,-458",
    "-485,-357,347",
    "-345,-311,381",
    "-661,-816,-575",
    "-876,649,763",
    "-618,-824,-621",
    "553,345,-567",
    "474,580,667",
    "-447,-329,318",
    "-584,868,-557",
    "544,-627,-890",
    "564,392,-477",
    "455,729,728",
    "-892,524,684",
    "-689,845,-530",
    "423,-701,434",
    "7,-33,-71",
    "630,319,-379",
    "443,580,662",
    "-789,900,-551",
    "459,-707,401",
    "",
    "--- scanner 1 ---",
    "686,422,578",
    "605,423,415",
    "515,917,-361",
    "-336,658,858",
    "95,138,22",
    "-476,619,847",
    "-340,-569,-846",
    "567,-361,727",
    "-460,603,-452",
    "669,-402,600",
    "729,430,532",
    "-500,-761,534",
    "-322,571,750",
    "-466,-666,-811",
    "-429,-592,574",
    "-355,545,-477",
    "703,-491,-529",
    "-328,-685,520",
    "413,935,-424",
    "-391,539,-444",
    "586,-435,557",
    "-364,-763,-893",
    "807,-499,-711",
    "755,-354,-619",
    "553,889,-390",
    "",
    "--- scanner 2 ---",
    "649,640,665",
    "682,-795,504",
    "-784,533,-524",
    "-644,584,-595",
    "-588,-843,648",
    "-30,6,44",
    "-674,560,763",
    "500,723,-460",
    "609,671,-379",
    "-555,-800,653",
    "-675,-892,-343",
    "697,-426,-610",
    "578,704,681",
    "493,664,-388",
    "-671,-858,530",
    "-667,343,800",
    "571,-461,-707",
    "-138,-166,112",
    "-889,563,-600",
    "646,-828,498",
    "640,759,510",
    "-630,509,768",
    "-681,-892,-333",
    "673,-379,-804",
    "-742,-814,-386",
    "577,-820,562",
    "",
    "--- scanner 3 ---",
    "-589,542,597",
    "605,-692,669",
    "-500,565,-823",
    "-660,373,557",
    "-458,-679,-417",
    "-488,449,543",
    "-626,468,-788",
    "338,-750,-386",
    "528,-832,-391",
    "562,-778,733",
    "-938,-730,414",
    "543,643,-506",
    "-524,371,-870",
    "407,773,750",
    "-104,29,83",
    "378,-903,-323",
    "-778,-728,485",
    "426,699,580",
    "-438,-605,-362",
    "-469,-447,-387",
    "509,732,623",
    "647,635,-688",
    "-868,-804,481",
    "614,-800,639",
    "595,780,-596",
    "",
    "--- scanner 4 ---",
    "727,592,562",
    "-293,-554,779",
    "441,611,-461",
    "-714,465,-776",
    "-743,427,-804",
    "-660,-479,-426",
    "832,-632,460",
    "927,-485,-438",
    "408,393,-506",
    "466,436,-512",
    "110,16,151",
    "-258,-428,682",
    "-393,719,612",
    "-211,-452,876",
    "808,-476,-593",
    "-575,615,604",
    "-485,667,467",
    "-680,325,-822",
    "-627,-443,-432",
    "872,-547,-609",
    "833,512,582",
    "807,604,487",
    "839,-516,451",
    "891,-625,532",
    "-652,-548,-490",
    "30,-46,-14",
]


def test_calculate_max_distance():
    scanner_2 = Scanner(2, [])
    scanner_2.position = (1105, -1205, 1229)
    scanner_3 = Scanner(3, [])
    scanner_3.position = (-92, -2380, -20)
    assert calculate_max_distance([scanner_2, scanner_3]) == 3621


def test_get_offset():
    edge_x = {1: AxisOffset(2, -1, 1), 2: AxisOffset(2, -1, 4)}
    edge_y = {1: AxisOffset(1, 1, 2), 2: AxisOffset(2, -1, 5)}
    edge_z = {1: AxisOffset(0, -1, 3), 2: AxisOffset(2, -1, 6)}

    assert get_offset(number=1, edges=(edge_x, edge_y, edge_z)) == (1, 2, 3)
    assert get_offset(number=2, edges=(edge_x, edge_y, edge_z)) == (4, 5, 6)


def test_apply_offset():
    coord_1 = (4, 5, 6)
    coord_2 = (1, 2, 3)
    offsets = (AxisOffset(2, -1, 1), AxisOffset(1, 1, 2), AxisOffset(0, -1, 3))
    assert apply_offset(coord_1, offsets, (1, 2, 3)) == (-5, 7, -1)
    assert apply_offset(coord_2, offsets, (1, 2, 3)) == (-2, 4, 2)


def test_get_scanners():
    assert len(get_scanners(test_input)) == 5


def test_process_scanners():
    scanners = get_scanners(test_input)
    assert scanners[0].position is not None
    assert scanners[1].position is None
    assert scanners[2].position is None
    assert scanners[3].position is None
    assert scanners[4].position is None

    process_scanners(scanners)

    assert scanners[0].position == (0, 0, 0)
    assert scanners[1].position == (68, -1246, -43)
    assert scanners[2].position == (1105, -1205, 1229)
    assert scanners[3].position == (-92, -2380, -20)
    assert scanners[4].position == (-20, -1133, 1061)


def test_count_unique_beacons():
    scanners = get_scanners(test_input)
    process_scanners(scanners)
    assert count_unique_beacons(scanners) == 79


def test_part_one():
    assert part_one(test_input) == 79


def test_part_two():
    assert part_two(test_input) == 3621
