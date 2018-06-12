qmodel.init('random')
policy.init('greedy')
for N episodes do:
        state = environment.init_episode()
        do:
            action = policy.select_action(state, qmodel) 
            (next_state, reward, done) = environment.step(state, action) 
            qmodel.learn((state, action, reward, next_state)) 
            state = next_state        
        while (!done)
end for