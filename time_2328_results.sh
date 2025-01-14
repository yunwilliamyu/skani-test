threads=1
bintime_var=/bin/time
#skani
$bintime_var -v -o times/skani_2328_triangle.time ./skani triangle -t$threads 2328/* > results/skani_2328

#mash
$bintime_var -v -o times/mash_2328_triangle.time mash triangle -p $threads 2328/*.fa > results/mash_2328

#fastani
$bintime_var -v -o times/fastani_2328_triangle.time fastANI --rl ./2328_l.txt --ql ./2328_l.txt -t $threads -o results/fastani_2328 --matrix

#sourmash 
rm -r 2328_sourmash_sketches
mkdir 2328_sourmash_sketches
$bintime_var -v -o times/sourmash_2328_sketch.time sourmash sketch dna 2328/*.fa --output-dir 2328_sourmash_sketches
$bintime_var -v -o times/sourmash_2328_triangle.time sourmash compare ./2328_sourmash_sketches/*.sig --max-containment --ani --csv results/sour_2328
sed -i "s/\,/\\t/g" results/sour_2328

#anim
$bintime_var -v -o times/anim_2328.time average_nucleotide_identity.py -m ANIm -i 2328/ -o results/2328-anim --workers $threads
