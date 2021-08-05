# RemoveUnclassified
# Language: Python
# Input: TXT
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin that takes as input a TXT file of taxa and counts.
Taxa are assumed to be represented on rows.
It then removes all taxa that are unclassified, producing the equivalent
TXT file with those taxa removed.
