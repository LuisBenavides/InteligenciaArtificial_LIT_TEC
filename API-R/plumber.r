#* Echo back the input
#* @param msg The message to echo
#* @get /echo
function(msg=""){
  # load the model
  super_model <- readRDS("./final_model.rds")
  #print(super_model)
  list(msg = paste0(super_model,": '", msg, "'"))
  # make a predictions on "new data" using the final model
  #final_predictions <- predict(super_model, validation[,1:60])
  #confusionMatrix(final_predictions, validation$Class)
  
  #list(msg = paste0("The message is: '", msg, "'"))
}

#* Plot a histogram
#* @png
#* @get /plot
function(){
  x <- rnorm(100)
  hist(x)
}

#* Return the sum of two numbers
#* @param a The first number to add
#* @param b The second number to add
#* @post /sum
function(validation){
  as.numeric(a) + as.numeric(b)
  # load the model
  super_model <- readRDS("./final_model.rds")
  
  # make a predictions on "new data" using the final model
  final_predictions <- predict(super_model, validation[,1:60])
  confusionMatrix(final_predictions, validation$Class)
}
