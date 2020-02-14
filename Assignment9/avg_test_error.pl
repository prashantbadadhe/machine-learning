$classifierFile ="pb498_assignment_random_hyperplane.py";
$dir = "G:/MyNjitData/sem1/ML-675-101/testData";
$data = "ionosphere";
$k=10000;
$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python $classifierFile $dir/$data/$data.data $dir/$data/$data.trainlabels.$i $k > nm_out.$data");
  $err[$i] = `perl error.pl $dir/$data/$data.labels nm_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Classifier error(mean, (std)) = $mean ($sd)\n";
