from measurement.measures import Weight

# lb to kg to lb
lbs = Weight(lb=173)
kgs = Weight(kg=lbs.kg)

print(lbs.lb == kgs.lb)

# kg to lb to kg
kgs = Weight(kg=40.5)
lbs = Weight(lb=kgs.lb)

print(lbs.kg == kgs.kg)
