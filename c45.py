def findDecision(obj): #obj[0]: Age, obj[1]: Gender, obj[2]: BMI, obj[3]: Region, obj[4]: No. Childred, obj[5]: Insurance Charges
	# {"feature": "Insurance Charges", "instances": 2369, "metric_value": 0.8757, "depth": 1}
	if obj[5]<=11619.334895939639:
		# {"feature": "Age", "instances": 1540, "metric_value": 0.3264, "depth": 2}
		if obj[0]<=47.126872135747675:
			# {"feature": "BMI", "instances": 1210, "metric_value": 0.0451, "depth": 3}
			if obj[2]<=39.829295303770365:
				# {"feature": "No. Childred", "instances": 1162, "metric_value": 0.04, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Region", "instances": 841, "metric_value": 0.0242, "depth": 5}
					if obj[3] == 'south':
						# {"feature": "Gender", "instances": 424, "metric_value": 0.0432, "depth": 6}
						if obj[1] == 'male':
							return 'no'
						elif obj[1] == 'female':
							return 'no'
						else: return 'no'
					elif obj[3] == 'north':
						return 'no'
					else: return 'no'
				elif obj[4]>4:
					# {"feature": "Gender", "instances": 321, "metric_value": 0.0764, "depth": 5}
					if obj[1] == 'male':
						return 'no'
					elif obj[1] == 'female':
						# {"feature": "Region", "instances": 64, "metric_value": 0.273, "depth": 6}
						if obj[3] == 'north':
							return 'no'
						elif obj[3] == 'south':
							return 'no'
						else: return 'no'
					else: return 'no'
				else: return 'no'
			elif obj[2]>39.829295303770365:
				# {"feature": "No. Childred", "instances": 48, "metric_value": 0.1461, "depth": 4}
				if obj[4]>1:
					return 'no'
				elif obj[4]<=1:
					# {"feature": "Gender", "instances": 20, "metric_value": 0.2864, "depth": 5}
					if obj[1] == 'female':
						return 'no'
					elif obj[1] == 'male':
						# {"feature": "Region", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[3] == 'north':
							return 'no'
						elif obj[3] == 'south':
							return 'no'
						else: return 'no'
					else: return 'no'
				else: return 'no'
			else: return 'no'
		elif obj[0]>47.126872135747675:
			# {"feature": "No. Childred", "instances": 330, "metric_value": 0.8277, "depth": 3}
			if obj[4]<=4:
				# {"feature": "BMI", "instances": 320, "metric_value": 0.8012, "depth": 4}
				if obj[2]<=43.330075780648144:
					# {"feature": "Region", "instances": 313, "metric_value": 0.789, "depth": 5}
					if obj[3] == 'south':
						# {"feature": "Gender", "instances": 230, "metric_value": 0.847, "depth": 6}
						if obj[1] == 'female':
							return 'no'
						elif obj[1] == 'male':
							return 'no'
						else: return 'no'
					elif obj[3] == 'north':
						# {"feature": "Gender", "instances": 83, "metric_value": 0.5643, "depth": 6}
						if obj[1] == 'male':
							return 'no'
						elif obj[1] == 'female':
							return 'no'
						else: return 'no'
					else: return 'no'
				elif obj[2]>43.330075780648144:
					# {"feature": "Region", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3] == 'north':
						# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1] == 'male':
							return 'no'
						elif obj[1] == 'female':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'south':
						return 'yes'
					else: return 'yes'
				else: return 'yes'
			elif obj[4]>4:
				# {"feature": "BMI", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[2]>29.72643633:
					return 'yes'
				elif obj[2]<=29.72643633:
					return 'no'
				else: return 'no'
			else: return 'yes'
		else: return 'no'
	elif obj[5]>11619.334895939639:
		# {"feature": "No. Childred", "instances": 829, "metric_value": 0.8365, "depth": 2}
		if obj[4]<=3:
			# {"feature": "BMI", "instances": 627, "metric_value": 0.7394, "depth": 3}
			if obj[2]<=42.48960714980578:
				# {"feature": "Age", "instances": 614, "metric_value": 0.7478, "depth": 4}
				if obj[0]>45.18403908794788:
					# {"feature": "Gender", "instances": 338, "metric_value": 0.8317, "depth": 5}
					if obj[1] == 'female':
						# {"feature": "Region", "instances": 180, "metric_value": 0.82, "depth": 6}
						if obj[3] == 'south':
							return 'yes'
						elif obj[3] == 'north':
							return 'yes'
						else: return 'yes'
					elif obj[1] == 'male':
						# {"feature": "Region", "instances": 158, "metric_value": 0.8445, "depth": 6}
						if obj[3] == 'south':
							return 'yes'
						elif obj[3] == 'north':
							return 'yes'
						else: return 'yes'
					else: return 'yes'
				elif obj[0]<=45.18403908794788:
					# {"feature": "Region", "instances": 276, "metric_value": 0.6153, "depth": 5}
					if obj[3] == 'south':
						# {"feature": "Gender", "instances": 146, "metric_value": 0.7328, "depth": 6}
						if obj[1] == 'female':
							return 'yes'
						elif obj[1] == 'male':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'north':
						# {"feature": "Gender", "instances": 130, "metric_value": 0.4441, "depth": 6}
						if obj[1] == 'male':
							return 'yes'
						elif obj[1] == 'female':
							return 'yes'
						else: return 'yes'
					else: return 'yes'
				else: return 'yes'
			elif obj[2]>42.48960714980578:
				return 'yes'
			else: return 'yes'
		elif obj[4]>3:
			# {"feature": "Age", "instances": 202, "metric_value": 0.9914, "depth": 3}
			if obj[0]<=60.63056664282543:
				# {"feature": "BMI", "instances": 200, "metric_value": 0.9896, "depth": 4}
				if obj[2]>18.3:
					# {"feature": "Region", "instances": 199, "metric_value": 0.9903, "depth": 5}
					if obj[3] == 'south':
						# {"feature": "Gender", "instances": 126, "metric_value": 0.9883, "depth": 6}
						if obj[1] == 'male':
							return 'no'
						elif obj[1] == 'female':
							return 'no'
						else: return 'no'
					elif obj[3] == 'north':
						# {"feature": "Gender", "instances": 73, "metric_value": 0.783, "depth": 6}
						if obj[1] == 'male':
							return 'yes'
						elif obj[1] == 'female':
							return 'yes'
						else: return 'yes'
					else: return 'yes'
				elif obj[2]<=18.3:
					return 'yes'
				else: return 'yes'
			elif obj[0]>60.63056664282543:
				return 'no'
			else: return 'no'
		else: return 'yes'
	else: return 'yes'



result = findDecision([433245,'female',30.5,'north',0,32453246346435.022])

print ("result : " , result)