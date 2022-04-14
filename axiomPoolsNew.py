import random

import numpy as np
from collections import defaultdict
import os
import timeit
import argparse

def readtrainfile(file):
    triples = []
    hr_t = defaultdict(set)
    ht_r = defaultdict(set)
    h_t = defaultdict(set)
    t_h = defaultdict(set)
    r_hrt = defaultdict(list)
    f = open(file, 'r', encoding='utf-8')
    for line in f.readlines():
        h, r, t = line.strip().split('\t')
        triples.append((h, r, t))
        hr_t[(h, r)].add(t)
        ht_r[(h, t)].add(r)
        h_t[h].add(t)
        t_h[t].add(h)
        r_hrt[r].append((h, r, t))
    return triples, hr_t, ht_r, h_t, t_h, r_hrt


def generateAxioms(triple_data, p, g, dataset_dir):
    triples, hr_t, ht_r, h_t, t_h, r_hrt = triple_data
    num_axiom_types = 10
    reflexive, symmetric, transitive, \
    equivalent, inverse, subProperty, \
    inferenceChain1, inferenceChain2, \
    inferenceChain3, inferenceChain4 = [set() for i in range(num_axiom_types)]
    count = 0

    # 关系组成字典
    realtionCos = {}

    for rel in r_hrt.keys():
        N = len(r_hrt[rel])
        pN = p * N
        num_samples = round(N - N * pow(1 - g, 1 / pN))
        np.random.shuffle(r_hrt[rel])
        num_triples = min(num_samples, len(r_hrt[rel]))
        print("num_triples", num_triples)
        hrts = r_hrt[rel][:num_triples]
        # 每轮打印
        if count % 1 == 0:
            print('num:%d / reflexive:%d / symmetric:%d '
                  '/ transitive:%d / inverse:%d / equivalent: %d '
                  '/ subProperty: %d/ inferenceChain1: %d '
                  '/ inferenceChain2: %d / inferenceChain3: %d '
                  '/ inferenceChain4: %d'
                % (count, len(reflexive), len(symmetric),
                   len(transitive), len(inverse), len(equivalent),
                    len(subProperty), len(inferenceChain1),
                   len(inferenceChain2), len(inferenceChain3),
                    len(inferenceChain4)))

        count_triples = 0
        for h, r, t in hrts:
            print(count_triples, end='\r')
            count_triples += 1

            # 1 relexive
            if h == t:
                reflexive.add((r,))
                # reflexive.add((h, r, t, h, r, t))

                key = str(r) + "+" + str(r)
                score = 0
                if key in realtionCos:
                    score = realtionCos[key]
                else:
                    score = str(random.uniform(0.9, 1.0))
                    realtionCos[key] = score

                line_new = str(2) + "\t" + "(" + h + "\t" + r + "\t" + t + ")" \
                "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"

                with open("two.txt", "a", encoding="utf-8") as fa:
                    fa.write(line_new)

            # 2 symmetric
            if (t, r, h) in r_hrt[r]:
                symmetric.add((r,))
                # symmetric.add((t, r, h, h, r, t))
                key = str(r) + "+" + str(r)
                score = 0
                if key in realtionCos:
                    score = realtionCos[key]
                else:
                    score = str(random.uniform(0.9, 1.0))
                    realtionCos[key] = score

                line_new = str(2) + "\t" + "(" + t + "\t" + r + "\t" + h + ")" \
                "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"

                with open("two.txt", "a", encoding="utf-8") as fa:
                    fa.write(line_new)

            # 3 transitive
            for t_tmp in hr_t[(h, r)]:
                if t_tmp != t and (t_tmp, r, t) in r_hrt[r]:
                    transitive.add((r,))
                    # transitive.add((t_tmp, r, t, h, r, t))

                    key = str(r) + "+" + str(r)
                    score = 0
                    if key in realtionCos:
                        score = realtionCos[key]
                    else:
                        score = str(random.uniform(0.9, 1.0))
                        realtionCos[key] = score

                    line_new = str(2) + "\t" + "(" + t_tmp + "\t" + r + "\t" + t + ")" \
                    "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                    with open("two.txt", "a", encoding="utf-8") as fa:
                        fa.write(line_new)

            # 4 equivalent and 6 subProperty
            for r_tmp in ht_r[(h, t)]:
                if r_tmp != r:
                    equivalent.add((r, r_tmp))
                    subProperty.add((r, r_tmp))
                    # equivalent.add((h, r_tmp, t, h, r, t))
                    # subProperty.add((h, r_tmp, t, h, r, t))

                    key = str(r_tmp) + "+" + str(r)
                    score = 0
                    if key in realtionCos:
                        score = realtionCos[key]
                    else:
                        score = str(random.uniform(0.9, 1.0))
                        realtionCos[key] = score

                    line_new = str(2) + "\t" + "(" + h + "\t" + r_tmp + "\t" + t + ")" \
                    "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                    with open("two.txt", "a", encoding="utf-8") as fa:
                        fa.write(line_new)

            # 5 inverse
            if (t, h) in ht_r.keys():
                for r_tmp in ht_r[(t, h)]:
                    inverse.add((r, r_tmp))
                    # inverse.add((t, r_tmp, h, h, r, t))

                    key = str(r_tmp) + "+" + str(r)
                    score = 0
                    if key in realtionCos:
                        score = realtionCos[key]
                    else:
                        score = str(random.uniform(0.9, 1.0))
                        realtionCos[key] = score

                    line_new = str(2) + "\t" + "(" + t + "\t" + r_tmp + "\t" + h + ")" \
                    "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                    with open("two.txt", "a", encoding="utf-8") as fa:
                        fa.write(line_new)

            # 7 inferenceChain
            # h --> e --> t
            h_e = h_t[h]
            t_e = t_h[t]
            e_common = h_e.intersection(t_e)
            # for e in e_common:
            #     for r1 in ht_r[(h, e)]:
            #         for r2 in ht_r[(e, t)]:
            #             inferenceChain.add((r, r1, r2))
            for e in e_common:
                # h -> e -> t
                for r1 in ht_r[(h, e)]:
                    for r2 in ht_r[(e, t)]:
                        inferenceChain3.add((r, r1, r2))
                        # inferenceChain3.add((h, r1, e, e, r2, t, h, r, t))

                        key = str(r1) + "+" + str(r2) + "+" + str(r)
                        score = 0
                        if key in realtionCos:
                            score = realtionCos[key]
                        else:
                            score = str(random.uniform(0.9, 1.0))
                            realtionCos[key] = score


                        s = str(3) + "\t" + "(" + h + "\t" + r1 + "\t" + e + ")" \
                            "\t" + "(" + e + "\t" + r2 + "\t" + t + ")" + \
                            "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                        with open("groundings.txt", "a", encoding="utf-8") as fa:
                            fa.write(s)

                # h <- e -> t
                for r1 in ht_r[(e, h)]:
                    for r2 in ht_r[(e, t)]:
                        inferenceChain1.add((r, r1, r2))
                        # inferenceChain1.add((e, r1, h, e, r2, t, h, r, t))

                        key = str(r1) + "+" + str(r2) + "+" + str(r)
                        score = 0
                        if key in realtionCos:
                            score = realtionCos[key]
                        else:
                            score = str(random.uniform(0.9, 1.0))
                            realtionCos[key] = score

                        s = str(3) + "\t" + "(" + e + "\t" + r1 + "\t" + h + ")" \
                            "\t" + "(" + e + "\t" + r2 + "\t" + t + ")" + \
                            "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                        with open("groundings.txt", "a", encoding="utf-8") as fa:
                            fa.write(s)

                # h <- e <- t
                for r1 in ht_r[(e, h)]:
                    for r2 in ht_r[(t, e)]:
                        inferenceChain2.add((r, r1, r2))
                        # inferenceChain2.add((e, r1, h, t, r2, e, h, r, t))

                        key = str(r1) + "+" + str(r2) + "+" + str(r)
                        score = 0
                        if key in realtionCos:
                            score = realtionCos[key]
                        else:
                            score = str(random.uniform(0.9, 1.0))
                            realtionCos[key] = score

                        s = str(3) + "\t" + "(" + h + "\t" + r1 + "\t" + e + ")" \
                            "\t" + "(" + t + "\t" + r2 + "\t" + e + ")" + \
                            "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                        with open("groundings.txt", "a", encoding="utf-8") as fa:
                            fa.write(s)

                # h -> e <- t
                for r1 in ht_r[(h, e)]:
                    for r2 in ht_r[(t, e)]:
                        inferenceChain4.add((r, r1, r2))
                        # inferenceChain4.add((h, r1, e, t, r2, e, h, r, t))

                        key = str(r1) + "+" + str(r2) + "+" + str(r)
                        score = 0
                        if key in realtionCos:
                            score = realtionCos[key]
                        else:
                            score = str(random.uniform(0.9, 1.0))
                            realtionCos[key] = score

                        s = str(3) + "\t" + "(" + h + "\t" + r1 + "\t" + e + ")" \
                            "\t" + "(" + t + "\t" + r2 + "\t" + e + ")" + \
                            "\t" + "(" + h + "\t" + r + "\t" + t + ")" + "\t" + score + "\n"
                        with open("groundings.txt", "a", encoding="utf-8") as fa:
                            fa.write(s)

        count += 1
        if count > 3:
            break

    print('finish processing')
    print('write reflexive file')
    writefile(reflexive, os.path.join(dataset_dir, 'axiom_pool/axiom_aeflexive.txt'), 1)
    print('write symmetric file')
    writefile(symmetric, os.path.join(dataset_dir, 'axiom_pool/axiom_symmetric.txt'), 1)
    print('write transitive file')
    writefile(transitive, os.path.join(dataset_dir, 'axiom_pool/axiom_transitive.txt'), 1)
    print('write inverse file')
    writefile(inverse, os.path.join(dataset_dir, 'axiom_pool/axiom_inverse.txt'), 2)
    print('write equivalent file')
    writefile(equivalent, os.path.join(dataset_dir, 'axiom_pool/axiom_equivalent.txt'), 2)
    print('write subProperty file')
    writefile(subProperty, os.path.join(dataset_dir, 'axiom_pool/axiom_subProperty.txt'), 2)
    print('write inferenceChain1 file')
    writefile(inferenceChain1, os.path.join(dataset_dir, 'axiom_pool/axiom_inferenceChain1.txt'), 3)
    print('write inferenceChain2 file')
    writefile(inferenceChain2, os.path.join(dataset_dir, 'axiom_pool/axiom_inferenceChain2.txt'), 3)
    print('write inferenceChain3 file')
    writefile(inferenceChain3, os.path.join(dataset_dir, 'axiom_pool/axiom_inferenceChain3.txt'), 3)
    print('write inferenceChain4 file')
    writefile(inferenceChain4, os.path.join(dataset_dir, 'axiom_pool/axiom_inferenceChain4.txt'), 3)

def writefile(axioms, file, num_element):
    with open(file, 'w', encoding='utf-8') as f:
        for obj in axioms:
            for i in range(num_element):
                f.write(obj[i])
                if i == num_element - 1:
                    f.write('\n')
                else:
                    f.write('\t')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Experiment setup')
    parser.add_argument('--dataset_dir', dest='dataset_dir', type=str, default='ROANicews05-15\\ROANicews05-15\\')
    parser.add_argument('--train_file', dest='train_file', type=str, default='rule-train.txt')
    parser.add_argument('--axiom_probability', dest='axiom_probability', type=float, default=0.5)
    parser.add_argument('--axiom_proportion', dest='axiom_proportion', type=float, default=0.95)
    option = parser.parse_args()
    file_train = os.path.join(option.dataset_dir, option.train_file)
    start = timeit.default_timer()
    p = option.axiom_probability
    g = option.axiom_proportion
    triple_data = readtrainfile(file_train)
    generateAxioms(triple_data, p, g, option.dataset_dir)
    end = timeit.default_timer()
    print('cost time:', end - start)
