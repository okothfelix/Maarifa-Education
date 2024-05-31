function sign_up(){
    var contents = '<h1 class="text-center mb-1">Sign Up.</h1><br><p class="text-center mb-5">If your institution is not using <strong>Maarifa Edu</strong> you can let us know by contacting us on <strong>+254 797 634 087</strong> or sending us an email @ <strong>support@maarifaedu.co.ke.</strong></p><form class="login-signup-form"><p class="text-center"><small class="text-muted text-center">Already have an account? <a href="javascript:void(0);" onclick="password_sign_in();">Sign in</a>.</small></p></form>';
    document.getElementById('login-details').innerHTML = contents;
}

function sign_in(){
   var user_name = document.getElementById('username').value;
   var password = document.getElementById('password').value;
   $.ajax({
        url:'https://maarifaedu.co.ke/login',
        type:'POST',
        data:{'email':user_name, 'password':password},
        success: function(response) {
                    document.getElementById('output').innerHTML = response;
        }
   });
}

function forgot_password(){
    var contents = '<h1 class="text-center mb-1">Recover Password</h1><p class="text-center mb-5">Access your account password.</p><form class="login-signup-form"><div class="form-group"><label class="pb-1">Username</label><div class="input-group input-group-merge"><div class="input-icon"><span class="ti-email"></span></div><input id="username" type="email" class="form-control" placeholder="username@yourinstitution" required></div></div><button type="submit" class="btn btn-block btn-round secondary-solid-btn border-radius mt-4 mb-3" onclick="password_recovery();">Recover Password</button><p class="text-center"><small class="text-muted text-center">Remember It? <a href="javascript:void(0);" onclick="password_sign_in();">Sign in</a>.</small></p></form>';
    document.getElementById('login-details').innerHTML = contents;
}

function password_sign_in(){
    var contents = '<h1 class="text-center mb-1">Sign In</h1><p class="text-center mb-5">Access your institution dashboard.</p><form class="login-signup-form"><div class="form-group"><label class="pb-1">Username</label><div class="input-group input-group-merge"><div class="input-icon"><span class="ti-email"></span></div><input id="username" type="email" class="form-control" placeholder="username@yourinstitution" required></div></div><div class="form-group"><div class="row"><div class="col"><label class="pb-1">Password</label></div><div class="col-auto"><a href="javascript:void(0);" onclick="forgot_password();">Forgot password?</a></div></div><div class="input-group input-group-merge"><div class="input-icon"><span class="ti-lock"></span></div><input id="password" type="password" class="form-control" placeholder="Enter your password" required></div></div><button type="submit" class="btn btn-block btn-round secondary-solid-btn border-radius mt-4 mb-3" onclick="sign_in();">Sign in</button><p class="text-center"><small class="text-muted text-center">Do not have an account yet? <a href="javascript:void(0);" onclick="sign_up();">Sign up</a>.</small></p></form>';
    document.getElementById('login-details').innerHTML = contents;
}

function password_recovery(){
    var user_name = document.getElementById('').value;

}

function password_recovery(){
    var email_address = document.getElementById('email').value;
}