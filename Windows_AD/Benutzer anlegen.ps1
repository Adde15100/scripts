Import-Module ActiveDirectory
$password = "Start123#" | ConvertTo-SecureString -AsPlainText -Force
$Import = Import-Csv ".\Benutzer.csv"
$dom = Get-ADDomain 
$dns = $dom.dnsroot



Foreach ($User in $Import)

{
$user.enabled=[System.Convert]::ToBoolean($user.enabled)
$user.changepasswordatlogon=[System.Convert]::ToBoolean($user.changepasswordatlogon)
$user.CannotchangePassword=[System.Convert]::ToBoolean($user.CannotchangePassword)
$user.Passwordnerverexpires=[System.Convert]::ToBoolean($user.Passwordnerverexpires)

$usr = $user.UserPrinzipalName + "@" + $dns

New-ADUser -AccountPassword $password -Name $User.name -GivenName $User.GivenName -Surname $User.Surname -UserPrincipalName $usr  -DisplayName $user.displayname -Enabled $user.enabled -ChangePasswordAtLogon $user.ChangePasswordatlogon -CannotChangePassword $user.CannotchangePassword -PasswordNeverExpires $user.Passwordnerverexpires -Description $user.Description
Add-ADGroupMember -Identity $user.Gruppe1 -Members $user.name
Add-ADGroupMember -Identity $user.Gruppe2 -Members $user.name
Add-ADGroupMember -Identity $user.Gruppe3 -Members $user.name


}


Write-Host "Zum Beenden bitte beliebige Taste drücken!"
$null=$Host.Ui.RawUI.ReadKey('NoEcho,IncludeKeyDown')



