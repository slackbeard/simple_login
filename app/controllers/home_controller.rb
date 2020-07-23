class HomeController < ApplicationController
  def index
    unless user_signed_in? 
      puts 'hi'
    end
  end
end
