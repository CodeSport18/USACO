for _ in range(int(input())):
	word_num, comma_num, period_num = [int(i) for i in input().split()]
	words = {
		"noun": [],
		"transitive-verb": [],
		"intransitive-verb": [],
		"conjunction": [],
	}
	for _ in range(word_num):
		token, type_ = input().split()
		words[type_].append(token)

	max_size = 0  # The largest number of words we can use
	# Along with how many TVs/ITVs bring about that largest size
	best_tv = 0
	best_itv = 0
	nouns = words["noun"]  # just a shorthand
	max_verbs = period_num + min(period_num, len(words["conjunction"]))
	# Test all combinations of transntive/intransitive verbs
	for tv in range(len(words["transitive-verb"]) + 1):
		for itv in range(len(words["intransitive-verb"]) + 1):
			nouns_left = len(nouns) - itv - 2 * tv
			if nouns_left < 0 or tv + itv > max_verbs:
				break

			# Try to use as many conjunctions as possible
			conj_used = min(len(words["conjunction"]), (tv + itv) // 2)
			# If a transitive verb was used, put nouns until we run out of commas
			extra = min(comma_num, nouns_left) if tv > 0 else 0
			total = 2 * itv + 3 * tv + extra + conj_used

			if total > max_size:
				max_size = total
				best_tv = tv
				best_itv = itv

	# Build all initial phrases (n + itv or n + tv + n)
	noun_at = 0
	phrases = []
	for i in range(best_itv):
		phrases.append(nouns[noun_at] + " " + words["intransitive-verb"][i])
		noun_at += 1
	for i in range(best_tv):
		noun1, noun2 = nouns[noun_at], nouns[noun_at + 1]
		noun_at += 2
		phrases.append(noun1 + " " + words["transitive-verb"][i] + " " + noun2)

	# Add as many nouns to the end of a tv-sentence as possible
	if best_tv > 0:
		last = [phrases[-1]]
		c = 0
		while c < comma_num and noun_at < len(nouns):
			last.append(", ")
			last.append(nouns[noun_at])
			noun_at += 1
			c += 1
		phrases[-1] = "".join(last)

	# Join all the sentences we can using conjunctions
	phrase_at = 0
	sentences = []
	for conj in words["conjunction"]:
		if phrase_at + 1 >= len(phrases):
			break
		first, second = phrases[phrase_at], phrases[phrase_at + 1]
		phrase_at += 2
		sentences.append(first + " " + conj + " " + second)
	sentences.extend(phrases[phrase_at:])

	print(max_size)
	res = ". ".join(sentences)
	res += "." if res else ""
	print(res)