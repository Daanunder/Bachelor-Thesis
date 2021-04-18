
class simulations(object):
    # Initial runs
    ## Simulation run 1205-3
    sim1205_3 = dict(
        netcdf_file = './data/temperature-variations/initial-model-1.2-1205-3/initial-model-1.2_map.nc', 
        run_id = '1205_3', 
        sal_min = 15, 
        sal_max = 25, 
        depth = 10, 
        layers=20
    )

    ## Simulation run 1305-1
    ## First run :%s/mesh2d_nLayers/mesh2d_nLayerss/g
    sim1305_1 = dict(
        netcdf_file = './data/temperature-variations/initial-model-1.4-1305-1/InitialModel_map.nc',
        run_id = '1305_1',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10
    )

    ## Simulation run 1305-2
    sim1305_2 = dict(
        netcdf_file = './data/temperature-variations/initial-model-1.4-1305-2/InitialModel_map.nc',
        run_id = '1305_2',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10
    )

    ## Simulation run 1305-3
    sim1305_3 = dict(
        netcdf_file = './data/temperature-variations/initial-model-1.4-1305-3/InitialModel_map.nc',
        run_id = '1305_3',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10
    )

    ## Simulation run 1305-4
    sim1305_4 = dict(
        netcdf_file = './data/temperature-variations/initial-model-1.4-1305-4/InitialModel_map.nc',
        run_id = '1305_4',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10
    )

    ## Simulation run 1305-5
    sim1305_5 = dict(
        netcdf_file = './data/temperature-variations/initial-model-1.4-1305-5/InitialModel_map.nc',
        run_id = '1305_5',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10
    )

    ## Simulation run 1305-6
    sim1305_6 = dict(
        netcdf_file = './data/z-layer variations/initial-model-1.4-1305-6/InitialModel_map.nc',
        run_id = '1305_6',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=20
    )

    ## Simulation run 1305-7
    sim1305_7 = dict(
        netcdf_file = './data/z-layer variations/initial-model-1.4-1305-7/InitialModel_map.nc',
        run_id = '1305_7',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=50
    )


    ## Simulation run 1305-8
    sim1305_8 = dict(
        netcdf_file = './data/z-layer variations/initial-model-1.4-1305-8/InitialModel_map.nc',
        run_id = '1305_8',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=100
    )

        
    # Reference model
    reference_model = {
    ## Simulation run 2605-1
    'sim2605_1':dict(
        netcdf_file = './data/reference-model/primary/InitialModel_map.nc',
        run_id = '2605_1',
        string_id = 'Reference model - Courant max = 0.7', 
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Reference model'
        ),

    ## Simulation run 1305-7
    'sim1305_7':dict(
        netcdf_file = './data/z-layer variations/initial-model-1.4-1305-7/InitialModel_map.nc',
        run_id = '1305_7',
        string_id = f'Δz = 0.2, Δx = 100, Courant = 0.7', 
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers = 50,
        delta_x = 100,
        parameter = 'None'
    ),
    
    ## Simulation run 2605-1
    'sim0206_1':dict(
        netcdf_file = './data/reference-model/3min/InitialModel_map.nc',
        run_id = '0206_1',
        string_id = 'Reference model - 3min output', 
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Reference model'
        ),

    ## Simulation run 1006-4
    'sim1006_4':dict(
        netcdf_file = './data/delta_x/1006-4/NewModel3000_map.nc',
        run_id = '1006_4',
        string_id = 'Reference model - Δx = 20m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 20,
        parameter = 'Reference model'
        ),

    ## Simulation run 1106-2
    'sim1106_2':dict(
        netcdf_file = './data/delta_z/1106-2/NewModel4000_map.nc',
        run_id = '1106_2',
        string_id = f'Reference model - Δz = {round(10/10,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 20,
        parameter = 'Reference model'
        )

    ## Simulation run 2605-1
    #'sim0206_1':dict(
        #netcdf_file = './data/reference-model/secondary/InitialModel_map.nc',
        #run_id = '1006_11',
        #string_id = 'Reference model - secondary', 
        #sal_min = 15,
        #sal_max = 25,
        #depth = 10,
        #layers=10,
        #delta_x = 100,
        #parameter = 'Reference model'
        #)


    ## Simulation run 2605-1
    #'sim0206_1':dict(
        #netcdf_file = './data/reference-model/3min/InitialModel_map.nc',
        #run_id = '0206_1',
        #string_id = 'Reference model - tertiary', 
        #sal_min = 15,
        #sal_max = 25,
        #depth = 10,
        #layers=10,
        #delta_x = 100,
        #parameter = 'Reference model'
        #)
    }

    # Courant numbers
    courant_numbers = {
        ## Simulation run 0106-1
        'sim0106_1':dict(
            netcdf_file = './data/courant-numbers/0106-1/InitialModel_map.nc',
            run_id = '0106_1',
            string_id = 'Max. Courant = 0.5', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-2
        'sim0106_2':dict(
            netcdf_file = './data/courant-numbers/0106-2/InitialModel_map.nc',
            run_id = '0106_2',
            string_id = 'Max. Courant = 0.6', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),
        
        ## Simulation run 0106-3
        'sim0106_3':dict(
            netcdf_file = './data/courant-numbers/0106-3/InitialModel_map.nc',
            run_id = '0106_3',
            string_id = 'Max. Courant = 0.8', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-4
        'sim0106_4':dict(
            netcdf_file = './data/courant-numbers/0106-4/InitialModel_map.nc',
            run_id = '0106_4',
            string_id = 'Max. Courant = 0.9', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-5
        'sim0106_5':dict(
            netcdf_file = './data/courant-numbers/0106-5/InitialModel_map.nc',
            run_id = '0106_5',
            string_id = 'Max. Courant = 1.0', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-6
        'sim0106_6':dict(
            netcdf_file = './data/courant-numbers/0106-6/InitialModel_map.nc',
            run_id = '0106_6',
            string_id = 'Max. Courant = 1.1', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-7
        'sim0106_7':dict(
            netcdf_file = './data/courant-numbers/0106-7/InitialModel_map.nc',
            run_id = '0106_7',
            string_id = 'Max. Courant = 1.2', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-8
        'sim0106_8':dict(
            netcdf_file = './data/courant-numbers/0106-8/InitialModel_map.nc',
            run_id = '0106_8',
            string_id = 'Max. Courant = 0.1', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-9
        'sim0106_9':dict(
            netcdf_file = './data/courant-numbers/0106-9/InitialModel_map.nc',
            run_id = '0106_9',
            string_id = 'Max. Courant = 0.2', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-10
        'sim0106_10':dict(
            netcdf_file = './data/courant-numbers/0106-10/InitialModel_map.nc',
            run_id = '0106_10',
            string_id = 'Max. Courant = 0.3', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-11
        'sim0106_11':dict(
            netcdf_file = './data/courant-numbers/0106-11/InitialModel_map.nc',
            run_id = '0106_11',
            string_id = 'Max. Courant = 0.4', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-12
        'sim0106_12':dict(
            netcdf_file = './data/courant-numbers/0106-12/InitialModel_map.nc',
            run_id = '0106_12',
            string_id = 'Max. Courant = 1.3', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-13
        'sim0106_13':dict(
            netcdf_file = './data/courant-numbers/0106-13/InitialModel_map.nc',
            run_id = '0106_13',
            string_id = 'Max. Courant = 1.4', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-14
        'sim0106_14':dict(
            netcdf_file = './data/courant-numbers/0106-14/InitialModel_map.nc',
            run_id = '0106_14',
            string_id = 'Max. Courant = 1.5', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-15
        'sim0106_15':dict(
            netcdf_file = './data/courant-numbers/0106-15/InitialModel_map.nc',
            run_id = '0106_15',
            string_id = 'Max. Courant = 1.6', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-16
        'sim0106_16':dict(
            netcdf_file = './data/courant-numbers/0106-16/InitialModel_map.nc',
            run_id = '0106_16',
            string_id = 'Max. Courant = 1.7', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-17
        'sim0106_17':dict(
            netcdf_file = './data/courant-numbers/0106-17/InitialModel_map.nc',
            run_id = '0106_17',
            string_id = 'Max. Courant = 1.8', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-18
        'sim0106_18':dict(
            netcdf_file = './data/courant-numbers/0106-18/InitialModel_map.nc',
            run_id = '0106_18',
            string_id = 'Max. Courant = 1.9', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            ),

        ## Simulation run 0106-19
        'sim0106_19':dict(
            netcdf_file = './data/courant-numbers/0106-19/InitialModel_map.nc',
            run_id = '0106_19',
            string_id = 'Max. Courant = 2.0', 
            sal_min = 15,
            sal_max = 25,
            depth = 10,
            layers=10,
            delta_x = 100,
            parameter = 'Max. Courant'
            )

        }
    
    # Time step size
    timestepsize = {

    ## Simulation run 0606-1
    'sim0606_1':dict(
        netcdf_file = './data/timestepsize/0606-1/InitialModel_map.nc',
        run_id = '0606_1',
        string_id = 'Δt = 10s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-2
    'sim0606_2':dict(
        netcdf_file = './data/timestepsize/0606-2/InitialModel_map.nc',
        run_id = '0606_2',
        string_id = 'Δt = 20s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),


    ## Simulation run 0606-3
    'sim0606_3':dict(
        netcdf_file = './data/timestepsize/0606-3/InitialModel_map.nc',
        run_id = '0606_3',
        string_id = 'Δt = 30s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-4
    'sim0606_4':dict(
        netcdf_file = './data/timestepsize/0606-4/InitialModel_map.nc',
        run_id = '0606_4',
        string_id = 'Δt = 40s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-5
    'sim0606_5':dict(
        netcdf_file = './data/timestepsize/0606-5/InitialModel_map.nc',
        run_id = '0606_5',
        string_id = 'Δt = 50s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-6
    'sim0606_6':dict(
        netcdf_file = './data/timestepsize/0606-6/InitialModel_map.nc',
        run_id = '0606_6',
        string_id = 'Δt = 60s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-7
    'sim0606_7':dict(
        netcdf_file = './data/timestepsize/0606-7/InitialModel_map.nc',
        run_id = '0606_7',
        string_id = 'Δt = 70s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-8
    'sim0606_8':dict(
        netcdf_file = './data/timestepsize/0606-8/InitialModel_map.nc',
        run_id = '0606_8',
        string_id = 'Δt = 80s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-9
    'sim0606_9':dict(
        netcdf_file = './data/timestepsize/0606-9/InitialModel_map.nc',
        run_id = '0606_9',
        string_id = 'Δt = 90s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-10
    'sim0606_10':dict(
        netcdf_file = './data/timestepsize/0606-10/InitialModel_map.nc',
        run_id = '0606_10', 
        string_id = 'Δt = 100s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-11
    'sim0606_11':dict(
        netcdf_file = './data/timestepsize/0606-11/InitialModel_map.nc',
        run_id = '0606_11',
        string_id = 'Δt = 200s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-12
    'sim0606_12':dict(
        netcdf_file = './data/timestepsize/0606-12/InitialModel_map.nc',
        run_id = '0606_12',
        string_id = 'Δt = 500s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-13
    'sim0606_13':dict(
        netcdf_file = './data/timestepsize/0606-13/InitialModel_map.nc',
        run_id = '0606_13',
        string_id = 'Δt = 1000s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-14
    'sim0606_14':dict(
        netcdf_file = './data/timestepsize/0606-14/InitialModel_map.nc',
        run_id = '0606_14',
        string_id = 'Δt = 5s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-15
    'sim0606_15':dict(
        netcdf_file = './data/timestepsize/0606-15/InitialModel_map.nc',
        run_id = '0606_15',
        string_id = 'Δt = 1s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-16
    'sim0606_16':dict(
        netcdf_file = './data/timestepsize/0606-16/InitialModel_map.nc',
        run_id = '0606_16',
        string_id = 'Δt = 0.1s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),


    ## Simulation run 0606-17
    'sim0606_17':dict(
        netcdf_file = './data/timestepsize/0606-17/InitialModel_map.nc',
        run_id = '0606_17',
        string_id = 'Δt = 250s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-18
    'sim0606_18':dict(
        netcdf_file = './data/timestepsize/0606-18/InitialModel_map.nc',
        run_id = '0606_18',
        string_id = 'Δt = 300s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-19
    'sim0606_19':dict(
        netcdf_file = './data/timestepsize/0606-19/InitialModel_map.nc',
        run_id = '0606_19',
        string_id = 'Δt = 350s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-20
    'sim0606_20':dict(
        netcdf_file = './data/timestepsize/0606-20/InitialModel_map.nc',
        run_id = '0606_20',
        string_id = 'Δt = 400s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-21
    'sim0606_21':dict(
        netcdf_file = './data/timestepsize/0606-21/NewModel4000_map.nc',
        run_id = '0606_21',
        string_id = 'Δt = 120s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-22
    'sim0606_22':dict(
        netcdf_file = './data/timestepsize/0606-22/NewModel4000_map.nc',
        run_id = '0606_22',
        string_id = 'Δt = 140s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),

    ## Simulation run 0606-23
    'sim0606_23':dict(
        netcdf_file = './data/timestepsize/0606-23/NewModel4000_map.nc',
        run_id = '0606_23',
        string_id = 'Δt = 160s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        ),
    ## Simulation run 0606-24
    'sim0606_24':dict(
        netcdf_file = './data/timestepsize/0606-24/NewModel4000_map.nc',
        run_id = '0606_24',
        string_id = 'Δt = 180s',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Time step size'
        )
    }

    delta_x = {

    ## Simulation run 1006-1
    'sim1006_1':dict(
        netcdf_file = './data/delta_x/1006-1/NewModel3000_map.nc',
        run_id = '1006_1',
        string_id = 'Δx = 5m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 5,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-2
    'sim1006_2':dict(
        netcdf_file = './data/delta_x/1006-2/NewModel3000_map.nc',
        run_id = '1006_2',
        string_id = 'Δx = 10m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 10,
        parameter = 'Resolution x-direction'
        ),

    ## Simulation run 1006-3
    'sim1006_3':dict(
        netcdf_file = './data/delta_x/1006-3/NewModel3000_map.nc',
        run_id = '1006_3',
        string_id = 'Δx = 16m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 16,
        parameter = 'Resolution x-direction'
        ),
    
    ## Simulation run 1006-5
    'sim1006_5':dict(
        netcdf_file = './data/delta_x/1006-5/NewModel3000_map.nc',
        run_id = '1006_5',
        string_id = 'Δx = 25m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 25,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-6
    'sim1006_6':dict(
        netcdf_file = './data/delta_x/1006-6/NewModel3000_map.nc',
        run_id = '1006_6',
        string_id = 'Δx = 31.25m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 31.25,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-7
    'sim1006_7':dict(
        netcdf_file = './data/delta_x/1006-7/NewModel3000_map.nc',
        run_id = '1006_7',
        string_id = 'Δx = 36.5m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 36.5,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-8
    'sim1006_8':dict(
        netcdf_file = './data/delta_x/1006-8/NewModel3000_map.nc',
        run_id = '1006_8',
        string_id = 'Δx = 40m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 40,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-9
    'sim1006_9':dict(
        netcdf_file = './data/delta_x/1006-9/NewModel3000_map.nc',
        run_id = '1006_9',
        string_id = 'Δx = 50m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 50,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-10
    'sim1006_10':dict(
        netcdf_file = './data/delta_x/1006-10/NewModel3000_map.nc',
        run_id = '1006_10',
        string_id = 'Δx = 62.5m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 62.5,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-11
    'sim1006_11':dict(
        netcdf_file = './data/delta_x/1006-11/NewModel3000_map.nc',
        run_id = '1006_11',
        string_id = 'Δx = 100m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 100,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-12
    'sim1006_12':dict(
        netcdf_file = './data/delta_x/1006-12/NewModel3000_map.nc',
        run_id = '1006_12',
        string_id = 'Δx = 200m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 200,
        parameter = 'Resolution x-direction'
        ),
    ## Simulation run 1006-13
    'sim1006_13':dict(
        netcdf_file = './data/delta_x/1006-13/NewModel3000_map.nc',
        run_id = '1006_13',
        string_id = 'Δx = 400m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=10,
        delta_x = 400,
        parameter = 'Resolution x-direction'
        )
    }

    delta_z = {

    ## Simulation run 1106-1
    'sim1106_1':dict(
        netcdf_file = './data/delta_z/1106-1/NewModel4000_map.nc',
        run_id = '1106_1',
        string_id = f'Δz = {round(10/5,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=5,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-4
    'sim1106_4':dict(
        netcdf_file = './data/delta_z/1106-4/NewModel4000_map.nc',
        run_id = '1106_4',
        string_id = f'Δz = {round(10/11,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=11,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-5
    'sim1106_5':dict(
        netcdf_file = './data/delta_z/1106-5/NewModel4000_map.nc',
        run_id = '1106_5',
        string_id = f'Δz = {round(10/12,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=12,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-6
    'sim1106_6':dict(
        netcdf_file = './data/delta_z/1106-6/NewModel4000_map.nc',
        run_id = '1106_6',
        string_id = f'Δz = {round(10/13,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=13,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-7
    'sim1106_7':dict(
        netcdf_file = './data/delta_z/1106-7/NewModel4000_map.nc',
        run_id = '1106_7',
        string_id = f'Δz = {round(10/15,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=15,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1006-8
    'sim1106_8':dict(
        netcdf_file = './data/delta_z/1106-8/NewModel4000_map.nc',
        run_id = '1106_8',
        string_id = f'Δz = {round(10/17,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=17,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-9
    'sim1106_9':dict(
        netcdf_file = './data/delta_z/1106-9/NewModel4000_map.nc',
        run_id = '1106_9',
        string_id = f'Δz = {round(10/20,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=20,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-10
    'sim1106_10':dict(
        netcdf_file = './data/delta_z/1106-10/NewModel4000_map.nc',
        run_id = '1106_10',
        string_id = f'Δz = {round(10/23,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=23,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),
    ## Simulation run 1106-11
    'sim1106_11':dict(
        netcdf_file = './data/delta_z/1106-11/NewModel4000_map.nc',
        run_id = '1106_11',
        string_id = f'Δz = {round(10/27,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=27,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),

    ## Simulation run 1106-12
    'sim1106_12':dict(
        netcdf_file = './data/delta_z/1106-12/NewModel4000_map.nc',
        run_id = '1106_12',
        string_id = f'Δz = {round(10/33,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=33,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        ),

    ## Simulation run 1106-13
    'sim1106_13':dict(
        netcdf_file = './data/delta_z/1106-13/NewModel4000_map.nc',
        run_id = '1106_13',
        string_id = f'Δz = {round(10/45,2)}m',
        sal_min = 15,
        sal_max = 25,
        depth = 10,
        layers=45,
        delta_x = 20,
        parameter = 'Resolution z-direction'
        )
    }

