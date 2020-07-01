# Before class

  * Thing 1 to do before class
  * Thing 2 to do before class

# Outline of class goals

  * Goal 1
  * Goal 2

# Class 


## Heading 1


```python
def rand_split_full(cluster_labels_bag, cluster_labels_full, split):
    merged_labels = cluster_labels_bag.merge(cluster_labels_full, on = 'URSI', how = 'left')
    merged_labels = merged_labels[merged_labels.split == split]
    rand = adjusted_rand_score(merged_labels.clust_bag, merged_labels.clust_no_bag)
    return([merged_labels, rand])
```


## Heading 2

Here is some `sample code`

# Challenge


